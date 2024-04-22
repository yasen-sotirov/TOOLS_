import {CustomerReview,
  Footer,
  Hero,
  PopularProducts,
  Services,
  SpecialOffer,
  Subscribe,
  SuperQuality,} from './sections';
import Nav from './components/Nav';


// този сетъп зачиства всичко и започван на бял лист
const App = () => (
  // релативен спрямо контейнета
  <main className="relative">
    <Nav />
    <section className="xl:padding-1
    wide:padding-r padding-b">
      <Hero />
    </section>

    <section className="padding">
      <PopularProducts />
    </section>

    <section className="padding">
      <SuperQuality />
    </section>

    <section className="padding-x py-10">
      <Services />
    </section>

    <section className="padding">
      <SpecialOffer />
    </section>

    <section className="bg-pale-blue padding">
      <CustomerReview />
    </section>

    <section className="padding-x sm:py-32 py-16 w-full">
      <Subscribe />
    </section>

    <section className="bg-black padding-x padding-t pb-8">
      <Footer />
    </section>

    <div class="bg-grey-50 mx-auto max-w-md overflow-hidden rounded-xl">
      <div class="md:flex">
        <div class="md:shrink-0">
          <span class="bg-orange-300 h-52 w-full object-cover md:h-full md:w-48" ></span>

          </div>
        </div>
        <div p-8>
          <a href="#" class="mt-1 block text-lg font-bold leading-tight text-gray-800">My awesome card</a>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique incidunt odio, consequatur tempore distinctio ad corrupti, suscipit deserunt eos odit facilis culpa debitis quas ipsa. Alias accusamus modi consectetur eum?</p>
        </div>
    </div>





  </main>







);

export default App;