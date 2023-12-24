import React from "react";
import isAuthCheck from "./tools";
import axios from "axios";
import {useNavigate} from "react-router-dom";

async function logoutUser() {
    try {
        const {data, status} = await axios.get (
            'http://localhost:8000/api/v1/token/logout',
                {
                    headers: {
                        Accept: 'application/json',
                    },
                    withCredentials: true
                }
        );
        localStorage.clear();
        return data;
    } catch (error) {
        if (axios.isAxiosError(error)) {
            console.log('error message: ', error.message);
            return error.message;
        }
    }
}


const Header = () => {
    let navigate = useNavigate();
    if (isAuthCheck()) {
        return (
            <header className="bg-white shadow">
                <div className="container mx-auto flex justify-between items-center py-4">
                    <div className="flex items-center">
                        <nav>
                            <a href={"/all-purchases"} className="text-lg font-semibold" style={{margin: "0 50px"}}>
                                Все покупки
                            </a>
                            <a href={"/cart"} className="text-lg font-semibold" style={{margin: "0 50px"}}>
                                Корзина покупок
                            </a>
                            <a href={"/"} className="text-lg font-semibold" style={{margin: "0 50px"}}>
                                Все товары
                            </a>
                            <button className="text-lg font-semibold" style={{margin: "0 50px"}} onClick={() => {
                                logoutUser();
                                navigate("/login");
                            }}>
                                Выйти из аккаунта
                            </button>
                        </nav>
                    </div>
                </div>
            </header>
        );
    } else {
        return (<div></div>);
    }
}


export default Header;
