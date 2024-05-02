/* NESTED ROUTERS
Връща инфо за номер ревю за номер продукт
http://localhost:3000/products/28/reviews/12 */

/* първо ще намери not found страница в текущата папка, 
ако няма ще намери външна такава */
import { notFound } from "next/navigation";

export default function ReviewDetail({
  params,
}: {
  // type hinting за овект с key-value
  params: {
    productid: string;
    reviewId: string;
  };
}) {
  // Ако търсеното ID е по-голямо от 1000 => 404
  if (parseInt(params.reviewId) > 1000) {
    notFound();
  }
  return (
    <h1>
      Review {params.reviewId} for product {params.productid}
    </h1>
  );
}
