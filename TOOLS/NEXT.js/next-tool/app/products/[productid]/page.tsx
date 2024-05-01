/* DYNAMIC ROUTERS
папката е в квадратни скоби и next я намапва
когато подадем име на продукта
http://localhost:3000/products/288
params.produxtid  се връзва с името на папката

в параметрите на функцията има type hinting -  показва че params е обект с 
пропъртита productid от тип стринг */

export default function ProductDetails ({params,}: {params: {productid: string}} ) {
    return (
        <h1>Details for product {params.productid}</h1>
    )
 }