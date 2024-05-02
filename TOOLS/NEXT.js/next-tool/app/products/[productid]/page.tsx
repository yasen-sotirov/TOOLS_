/* DYNAMIC ROUTERS
папката е в квадратни скоби и next я намапва
когато подадем име на продукта
http://localhost:3000/products/288
params.produxtid  се връзва с името на папката

в параметрите на функцията има type hinting -  показва че params е обект с 
пропъртита productid от тип стринг */

// https://www.youtube.com/watch?v=yE_y4EBq-EA&list=PLC3y8-rFHvwjOKd6gdf4QtV1uYNiQnruI&index=17&ab_channel=Codevolution

import { Metadata } from "next";
type Props = {
  params: {
    productId: string;
  };
};

export const generatedMetadata = ({ params }: Props): Metadata => {
  return {
    title: `Peoduct ${params.productId}`,
  };
};

export default function ProductDetails({
  params,
}: {
  params: { productid: string };
}) {
  return <h1>Details for product {params.productid}</h1>;
}
