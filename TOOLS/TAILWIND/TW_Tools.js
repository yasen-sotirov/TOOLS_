"TAILWIND"



"ИНСТАЛИРАНЕ"
/* https://tailwindcss.com/docs/installation
npm install -D tailwindcss
npx tailwindcss init


*/




"CLASSES"
/* 

RESPONSIVE DESIGN:
    активира се при минимум:
    sm	640px	@media (min-width: 640px) { ... }
    md	768px	@media (min-width: 768px) { ... }
    lg	1024px	@media (min-width: 1024px) { ... }
    xl	1280px	@media (min-width: 1280px) { ... }
    2xl	1536px	@media (min-width: 1536px) { ... }


 --=== ПРИМЕР ===--
https://tailwindcss.com/docs/responsive-design

<div class="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl">
  <div class="md:flex">
    <div class="md:shrink-0">
      <div class="bg-red-400 h-48 w-full object-cover md:h-full md:w-48">
      </div>

    </div>
    <div class="p-8">
      <div class="uppercase tracking-wide text-sm text-indigo-500 font-semibold">Company retreats</div>
      <a href="#" class="block mt-1 text-lg leading-tight font-medium text-black hover:underline">Incredible accommodation for your team</a>
      <p class="mt-2 text-slate-500">Looking to take your team away on a retreat to enjoy awesome food and take in some sunshine? We have a list of places to do just that.</p>
    </div>
  </div>
</div>



<div class="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl">` 
    max-w-md        - стилове за максимална ширина 
    mx-auto         - позициониране по центъра на страницата 
    bg-white        - цвят на заден план
    rounded-xl      - закръглени ъгли 
    shadow-md       - сянка
    overflow-hidden - скриване на препълвания текст
    md:max-w-2xl    - за екрани по-големи от medium максималната ширина е по-голяма

<div class="md:flex">
    md:flex         - използва flexbox само на екрани medium и по-големи

<div class="md:shrink-0">
    md:shrink-0     - да не се увеличава при гъвкавата аранжировка на flexbox в по-големи екрани



    

ИЗОБРАЖЕНИЕ
<div class="bg-red-400 h-48 w-full object-cover md:h-full md:w-48"></div>
    bg-red-400      - червен цвят на заден план 
    h-48            - височина от 48 пиксела 
    w-full          - ширина от 100% на родителския контейнер
    object-cover    - стил за покриване на съдържанието
    md:h-full       - за екрани medium и по-големи, височината е пълна височина 
    md:w-48         - за екрани medium и по-големи, широчината е 48 пиксела 
    object-cover:fit  вмества снимката в контейнера, като изрязва излишното от нея. не я мачка


ТЕКСТ
<div class="p-8"> 
    p-8             - вътрешни отстъпи от 8 пиксела 


ЗАГЛАВИЕ
<div class="uppercase tracking-wide text-sm text-indigo-500 font-semibold">Company retreats</div>
    uppercase       - да бъде в главни букви
    tracking-wide   - голям междулиниен интервал
    text-sm         - размер на шрифта  малък
    text-indigo-500 - син цвят на текста
    font-semibold   - и полужирен


ЛИНК
<a href="#" class="block mt-1 text-lg leading-tight font-medium text-black hover:underline">
Incredible accommodation for your team</a>
    block           - блоков елемент 
    mt-1            - отстъп от 1 пиксел
    text-lg         - голям размер на шрифта
    leading-tight   - тясно междуредие 
    font-medium     - среден тегло на шрифта
    text-black      - черен текст 
    hover:underline - подчертаване при ховър


АБЗАЦ ТЕКСТ
<p class="mt-2 text-slate-500">Looking to take your team ...</p>
    mt-2            - отстъп от 2 пиксела 
    text-slate-500  - сив цвят на текста




ПОДРАВНЯВАНЕ
    хоризонтално подравняване       - flex justify-content
    вертикално подравняване         - flex align-items






COLORS:
    палитра     - https://tailwindcss.com/docs/customizing-colors
    custom      - в tailwind.config.js като k-v в extend:{ } 
    


BORDER:
    border  - 0px
    border-2 4 8px
    border-green-500
    Use the ring-* utilities to set the color of an outline ring.



DARK MODE
dark:



TEXT:
    color       - text-green-50/900
    size        - text-xs(12) -sm(14) -base(16) -lg(18) -xl(20) -2xl(24) -3xl(30)
    tracking    - разстояние между буквите
    leading     - разстояние между редовете


FONT:
    app/globals.css  
        @import url("https://..)
    italic
    underline i dr  - https://tailwindcss.com/docs/text-decoration-thickness


PADDING растоянието в елемента:



SAVE CUSTOM
    theme: {
        extend: {
        },
        colors: {
            custom_green: {
            100: "#49e659",
            200: "#49e759",
            },
        fontSize{
            base: '1rem'
        }



ЦВЯТ НА СЕЛЕКТИРАН ТЕКСТ
selection:bg-fuchsia-300



IMPUT
    focus:outline-none      - премахва ограждението около текста докато пишеш



ПОЗИЦИЯ - указва местоположението на елемента
    top-0 left-0


BLOCK НАД СНИМКС
<div className="relative">
    <img src="Google.png" alt="Image" className="w-full h-auto"></img>
    <div className="absolute inset-0 flex items-center justify-center">
    <div class="bg-black bg-opacity-50 text-white p-4">
        Текст над снимката
    </div>
    </div>
</div>

*/
