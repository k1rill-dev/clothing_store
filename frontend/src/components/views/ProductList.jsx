import React from 'react';
import ProductCard from "./ProductCard";

const ProductList = ({  }) => {
  const products = [
  {
    name: "Apple iPhone 14 Pro Max",
    description: "The most advanced iPhone ever",
    image: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/IPhone_14_Pro_Max_%28front%29.jpg/1200px-IPhone_14_Pro_Max_%28front%29.jpg",
    price: 1.099
  },
  {
    name: "Samsung Galaxy S23 Ultra",
    description: "The best Android phone on the market",
    image: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Samsung_Galaxy_S23_Ultra_%28front%29.jpg/1200px-Samsung_Galaxy_S23_Ultra_%28front%29.jpg",
    price: 999
  },
  {
    name: "Google Pixel 7 Pro",
    description: "The best Pixel phone yet",
    image: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Samsung_Galaxy_S23_Ultra_%28front%29.jpg/1200px-Samsung_Galaxy_S23_Ultra_%28front%29.jpg",
    price: 899
  }
];
  return (
    <div className="flex flex-wrap justify-center mt-10">
      <h1 className="text-xl font-semibold mb-4">Products</h1>
      <ul className="flex flex-wrap justify-between mt-4">
        {products.map((product) => (
          <li key={product.id} className="flex flex-col justify-between w-full px-4 py-2">
            <ProductCard/>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;
