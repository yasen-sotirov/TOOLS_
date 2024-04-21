import { headerLogo} from '../assets/images';
import{hamburger} from '../assets/icons';
import { navLinks } from '../constants';

const Nav = () => {
  return (
    <heder className="padding-x
    py-8 absolute z-10 w-full">
      
      {/* logo */}
      <nav className="flex 
      justify-between
      items-center 
      max-container">
        <a href="/">
          <img 
            src={headerLogo} 
            alt='Logo'
            width={130}
            height={29}
            />
        </a>

        <ul className="flex-1 flex 
        justify-center items-center
        gap-16 max-lg:hidden">
          {navLinks.map((item) => (
            <li key={item.label}>
              <a href={item.href}
              className='font-monts
              errat leading-normal
              text-lg text-slate-gray'>
                {item.label}
              </a>
            </li>
          ))}
        </ul>
        <ul>
          {/* бургера е скрит, става на блок (показва се) над max-lg*/}
          <div className='hidden
          max-lg:block'>
            <img src={hamburger} alt="hamburger" width={25}
            height={25} />
          </div>
        </ul>
      </nav>
    </heder>
  )
}

export default Nav