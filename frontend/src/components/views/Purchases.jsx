import React from 'react';
import PurchaseCard from "./PurchaseCard";
import requesterXML from "../../utilities/requesterXML";

const Purchases = () => {
    const currentUserEmail = JSON.parse(localStorage.getItem("userInfo")).email
    let purchases = [];
    let furCoatPurchase = requesterXML("GET", "http://localhost:8000/api/v1/furcoat-sale/", false, null)
    // let bagPurchase = requesterXML("GET", "http://localhost:8000/api/v1/bag-sale/", false, null)
    // let hatPurchase = requesterXML("GET", "http://localhost:8000/api/v1/hat-sale/", false, null)
    // let glovesPurchase = requesterXML("GET", "http://localhost:8000/api/v1/gloves-sale/", false, null)
    purchases.push(furCoatPurchase)
    // purchases.push(bagPurchase)
    // purchases.push(hatPurchase)
    // purchases.push(glovesPurchase)
    console.log(purchases)
    return (
        <div className={"flex-col flex items-center bg-white gap-8 p-10 text-black text-sm"}>
            <h1 className="text-2xl font-bold">Все продажи</h1>
            {purchases.map((purchase, index) => (
                <PurchaseCard purchase={purchase} index={index}/>
            ))}
        </div>
    );
};

export default Purchases;