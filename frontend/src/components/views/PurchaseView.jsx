import React from "react";
import requesterXML from "../../utilities/requesterXML";
import {useParams} from "react-router-dom";

const PurchaseView = () => {
  let params = useParams();
  const id = Number(params.id);
  // let purchase = requester("GET", "")
  // let purchase = requester("GET", "")
  return (
    // <div className="flex flex-col items-start justify-center">
    //   <h2 className="text-3xl font-bold">Информация о покупке</h2>
    //   <div className="my-2">
    //     <div className="flex flex-col">
    //       <h3 className="text-2xl font-bold">Корзина</h3>
    //       <table className="table-auto w-full">
    //         <thead>
    //           <tr>
    //             <th className="text-left">Наименование</th>
    //             <th className="text-left">Количество</th>
    //             <th className="text-left">Цена</th>
    //           </tr>
    //         </thead>
    //         <tbody>
    //           {basket.map((item) => (
    //             <tr key={item.id}>
    //               <td className="text-left">{item.name}</td>
    //               <td className="text-left">{item.quantity}</td>
    //               <td className="text-left">{item.price}</td>
    //             </tr>
    //           ))}
    //         </tbody>
    //       </table>
    //     </div>
    //     <div className="flex flex-col">
    //       <h3 className="text-2xl font-bold">Дата продажи</h3>
    //       <p className="text-left">{date_sell}</p>
    //     </div>
    //     <div className="flex flex-col">
    //       <h3 className="text-2xl font-bold">Продавец</h3>
    //       <p className="text-left">{seller}</p>
    //     </div>
    //   </div>
    // </div>
      <div></div>
  );
};

export default PurchaseView;
