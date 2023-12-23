import {useState} from "react";
import React from "react";
import { useContext } from 'react'
import { CartContext } from '../../utilities/cart'


const Cart = ({ items, onItemRemove }) => {
  const { cartItems, addToCart, removeFromCart, clearCart, getCartTotal } = useContext(CartContext)
  // let sendData = []
  // cartItems.map((item) => {
  //   sendData.push({
  //     id: item.id,
  //     size: item.size,
  //     count: item.count,
  //     type: item.type
  //   })
  // })

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
              addToCart(item)
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
    <h1 className="text-lg font-bold">Всего: ${getCartTotal()}</h1>
    <button
      className="px-4 py-2 bg-gray-800 text-white text-xs font-bold uppercase rounded hover:bg-gray-700 focus:outline-none focus:bg-gray-700"
      onClick={() => {
        clearCart()
      }}
    >
      Очистить корзину
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
