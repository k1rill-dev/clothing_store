import React, {useEffect, useState} from 'react';
import ProductCard from "./ProductCard";
import axios from "axios";
import isAuthCheck from "./tools";
import {Navigate} from "react-router-dom";
import requesterXML from "../../utilities/requesterXML";


const ProductList = ({onAddItem}) => {
    let data = []
    let furcoat = requesterXML("GET", "http://localhost:8000/api/v1/furcoat/", false, null)
    furcoat.map((element) => {
        Object.assign(element, {type: "furcoat"})
    })
    let gloves = requesterXML("GET", "http://localhost:8000/api/v1/gloves/", false, null)
    gloves.map((element) => {
        Object.assign(element, {type: "gloves"})
    })
    let hat = requesterXML("GET", "http://localhost:8000/api/v1/hat/", false, null)
    hat.map((element) => {
        Object.assign(element, {type: "hat"})
    })
    let bag = requesterXML("GET", "http://localhost:8000/api/v1/bag/", false, null)
    bag.map((element) => {
        Object.assign(element, {type: "bag"})
    })
    data.push(furcoat)
    data.push(gloves)
    data.push(hat)
    data.push(bag)
    // console.log(data)
    data = data.flat(1)
    console.log(data)
    // console.log(onAddItem)
    if (isAuthCheck()) {
        return (
            <div className="flex flex-wrap mt-10">
                <ul className="flex flex-wrap justify-between mt-4">
                    {data.map((product) => (
                        <li key={product.id} className="flex flex-col justify-between w-full px-4 py-2">
                            <ProductCard product={product} onAddItem={onAddItem}/>
                        </li>
                    ))}
                </ul>
            </div>
        );
    }
    else{
        return (<Navigate to={"/login"}></Navigate>)
    }
}


export default ProductList;
