import React from "react";
import { CartContext } from '../../utilities/cart'
import { useContext, useEffect, useState } from 'react'


const ProductCard = ({product, onAddItem}) => {
  const { cartItems, addToCart } = useContext(CartContext)
  console.log(product)
    return (
        <div
      className="flex flex-col rounded-lg bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-neutral-700 md:max-w-xl md:flex-row">
      <img
        className="h-96 w-full rounded-t-lg object-cover md:h-auto md:w-48 md:rounded-none md:rounded-l-lg"
        src={"http://localhost:8000"+product.photos[0][0].image}
        alt="" />
      <div className="flex flex-col justify-start p-6">
        <h5
          className="mb-2 text-xl font-medium text-neutral-800 dark:text-neutral-50">
          {product.product.title}
        </h5>
        <p className="mb-4 text-base text-neutral-600 dark:text-neutral-200">
          {product.product.description} от {product.brand}
        </p>
          <p className="mb-4 text-base text-neutral-600 dark:text-neutral-200">
          Цена: {product.price}
        </p>
        <p className="text-xs text-neutral-500 dark:text-neutral-300">Доступные размеры:</p>
        <p className="text-xs text-neutral-500 dark:text-neutral-300">
          {product.product.sizes ? <div className="grid grid-cols-1 gap-6 sm:grid-cols-2">
                {product.product.sizes.map((size) => (
                      <p className="mb-3 text-gray-500 dark:text-gray-400">{size.size}</p>
                  ))}
            </div> : <div></div>}
        </p>
          <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onClick={() => addToCart(product)}>
          Добавить в корзину
        </button>
      </div>
    </div>
    );
};
export default ProductCard