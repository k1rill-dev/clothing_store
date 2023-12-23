import logo from './logo.svg';
import './App.css';
import React, {useState} from 'react'
import ReactDOM from 'react-dom'
import {BrowserRouter, Route, Routes} from "react-router-dom";
import ProductList from "./components/views/ProductList";
import Cart from "./components/views/Cart";
import Purchases from "./components/views/Purchases";
import Login from "./components/views/Login";
import Header from "./components/views/Header";
import PurchaseView from "./components/views/PurchaseView";


function App() {
    const [items, setItems] = useState([
        {
            id: 1,
            name: "Телефон",
            price: 10000,
            image: "/images/phone.png",
        },
        {
            id: 2,
            name: "Компьютер",
            price: 20000,
            image: "/images/computer.png",
        },
    ]);

    const onItemRemove = (id) => {
        setItems(items.filter((item) => item.id !== id));
    };
    const onAddItem = (item) => {
      setItems(item)
      //   console.log(item)
    }
    return (
        <BrowserRouter>
            <Routes>
                <Route path={"/"} element={(<div><Header/><ProductList onAddItem={onAddItem}/></div>)}/>
                <Route path={"/cart"} element={(<div><Header/><Cart items={items} onItemRemove={onItemRemove}/></div>)}/>
                <Route path={"/all-purchases"} element={(<div><Header/><Purchases/></div>)}/>
                <Route path={"/login"} element={(<div><Header/><Login/></div>)}/>
                <Route path="/purchase">
                    <Route path=":id" element={(
                        <div>
                            <Header/>
                            <PurchaseView/>
                        </div>
                    )}>
                    </Route>
                </Route>
            </Routes>
        </BrowserRouter>
    );
}

export default App;
