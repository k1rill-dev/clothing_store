import React from "react";

const Header = ({ allPurchasesLink, cartLink, allProductsLink }) => {
  return (
    <header className="bg-white shadow">
      <div className="container mx-auto flex justify-between items-center py-4">
        <div className="flex items-center">
          <a href={allPurchasesLink} className="text-lg font-semibold" style={{ margin: "0 100px" }}>
            Все покупки
          </a>
          <a href={cartLink} className="text-lg font-semibold" style={{ margin: "0 100px" }}>
            Корзина покупок
          </a>
          <a href={allProductsLink} className="text-lg font-semibold" style={{ margin: "0 100px" }}>
            Все товары
          </a>
        </div>
      </div>
    </header>
  );
};

export default Header;
