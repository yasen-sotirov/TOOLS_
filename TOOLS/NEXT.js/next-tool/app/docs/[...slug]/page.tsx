/* При така създадена файловата структура, 
ако в url ила docs ще ни доведе до тук  */

export default function Docs({
    params,
    }: {
        params: {
            slug: string[];
        };
    }) {
        if(params.slug.length ===2) {
            return (
                <h1>
                    View docs for frature {params.slug[0]} and concept {params.slug}
                </h1>
            );
        }
        else if (params.slug.length ===1) {
            return <h1>Viewing docs for feature {params.slug[]}</h1>
        }
        return (
            <h1>Docs home page !</h1>
            )}