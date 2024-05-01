/* NESTED ROUTERS
Връща инфо за номер ревю за номер продукт
http://localhost:3000/products/28/reviews/12 */

export default function ReviewDetail({params,}: {
    // type hinting за овект с key-value
    params: {
        productid: string;
        reviewId: string;
    };
}) {
    return (
        <h1>Review {params.reviewId} for product {params.productid}</h1>
    )
}