import {useState} from "react";
import React from "react";
import { useContext } from 'react'
import { CartContext } from '../../utilities/cart'
import axios from "axios";
import {getCookieValue} from "../../utilities/requesterXML"
import {useNavigate} from "react-router-dom";

const buy = async (cart) => {
  try {
    const {data, status} = await axios.post(
        'http://localhost:8000/api/v1/buy',
        cart,
        {
          headers: {
            'Content-Type': 'application/json',
            Accept: 'application/json',
            "X-CSRFToken": getCookieValue("csrftoken")
          },
          withCredentials: true
        }
    );
    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      console.log('error message: ', error.message);
      return error.message;
    } else {
      console.log('unexpected error: ', error);
      return 'An unexpected error occurred';
    }
  }
}

const Cart = ({ items, onItemRemove }) => {
  const { cartItems, addToCart, removeFromCart, clearCart, getCartTotal } = useContext(CartContext)
  let sendData = []
  cartItems.map((item) => {
    item.currentSize !== null
        ? sendData.push({
      product_id: item.id,
      size: item.currentSize.size,
      count: item.quantity,
      type: item.type,
      size_id: item.currentSize.id
    })
        : sendData.push({
      product_id: item.id,
      size: null,
      count: item.quantity,
      type: item.type,
      size_id: null
    })
  })
  let navigate = useNavigate();
  return (
    <div className="flex-col flex items-center bg-white gap-8 p-10 text-black text-sm">
  <h1 className="text-2xl font-bold">Корзина</h1>
  <div className="flex flex-col gap-4">
    {cartItems.map((item) => (
      <div className="flex justify-between items-center" key={item.id}>
        <div className="flex gap-4">
          <img src={"http://localhost:8000"+item.photos[0][0].image} alt={item.title} className="rounded-md h-24" />
          <div className="flex flex-col">
            <h1 className="text-lg font-bold">{item.product.title}</h1>
            <p className="text-gray-600">{item.price}</p>
          </div>
        </div>
        <div className="flex gap-4">
          <button
            className="px-4 py-2 bg-gray-800 text-white text-xs font-bold uppercase rounded hover:bg-gray-700 focus:outline-none focus:bg-gray-700"
            onClick={() => {
              addToCart(item, item.currentSize);
            }}
          >
            +
          </button>
          <p>{item.quantity}</p>
          <button
            className="px-4 py-2 bg-gray-800 text-white text-xs font-bold uppercase rounded hover:bg-gray-700 focus:outline-none focus:bg-gray-700"
            onClick={() => {
              removeFromCart(item)
            }}
          >
            -
          </button>
        </div>
      </div>
    ))}
  </div>
  {
    cartItems.length > 0 ? (
      <div className="flex flex-col justify-between items-center">
    <h1 className="text-lg font-bold">Всего: {getCartTotal()}₽</h1>
    <button
      className="px-4 py-2 bg-gray-800 text-white text-xs font-bold uppercase rounded hover:bg-gray-700 focus:outline-none focus:bg-gray-700"
      onClick={() => {
        clearCart()
      }}
      style={{marginBottom: 5}}
    >
      Очистить корзину
    </button>
        <button
      className="px-4 py-2 bg-gray-800 text-white text-xs font-bold uppercase rounded hover:bg-gray-700 focus:outline-none focus:bg-gray-700"
      onClick={() => {
        buy(sendData);
        navigate("/all-purchases");
      }}
    >
      Оформить покупку
    </button>
  </div>
    ) : (
      <h1 className="text-lg font-bold">Ваша корзина пуста</h1>
    )
  }
</div>

  );
};

export default Cart;
