const Hero = () => {
  return (
    <section
    id="home"
    // за да заеме целия екран
    // flex         - за флекс контейнер
    // xl:flex-row  - при големи екрани става на колона
    // flex-col     - става на колона при мобилни устр
    // justify-center - центрира съдържанието
    // min-h-screen   - минимална височина - цял екран
    // max-container  - собствен контейнер. над тази резолюция ще се свие до 1440пж
    className="w-full 
    flex  
    xl:flex-row
    flex-col
    justify-center min-h-screen
    max-container">

    {/* xl:w-2/5  при екстра големи у-ва ширината ще е 2/5 от екрана 
      items-start   елементите ще се подреждат вертикално */}
    <div className="relative
    xl:w-2/5 flex flex-col
    justify-center items-start
    w-full max-xl:padding-x pt-28">
      <p>Our Summer Collection</p>
      <h1>
        <span>The new Arrivel</span>
        <br />
        <span>Mike Shoes</span>
      </h1>

      1;21q
    </div>
    </section>
  )
}

export default Hero