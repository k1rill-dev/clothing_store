import React from 'react';
import {Link} from "react-router-dom";

const PurchaseCard = ({purchase, index}) => {
  // console.log(purchase)
  let sum = 0;
  purchase.basket.forEach((element) => {
    sum+=element.price
  })
    return (
        <div className="max-w-sm w-full lg:max-w-full lg:flex">
  <div className="border-r border-b border-l border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
    <div className="text-gray-900 font-bold text-xl mb-2">Проданные товары:</div>
    <div className={"grid grid-cols-1 sm:grid-cols-2"}>
      {purchase.basket.map((element) => (
          <p className="mb-3 text-gray-500 dark:text-gray-400">{element.product.title}</p>
      ))}
    </div>
    <div className="mb-8">
      <p className="text-gray-700 text-base">Полная стоимость - {sum}₽</p>
      <p className="text-gray-700 text-base">Количество проданных товаров - {purchase.count}</p>
    </div>
    <div className="flex items-center">
      <div className="text-sm">
        <p className="text-gray-900 leading-none">Кто продал - {purchase.seller.email}</p>
        <p className="text-gray-600">Когда продал - {purchase.date_sell}</p>
      </div>
    </div>
    <Link to={"/purchase/" + purchase.id}>
       <button className={"bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"}>
    Посмотреть покупку
    </button>
    </Link>
  </div>
</div>

    );
};

export default PurchaseCard;