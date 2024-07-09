import logo from '../assets/KangacookLogo.png'
const LogoNav = () => {

    return (
        <div className="h-32 bg-zinc-50 w-screen flex justify-center items-center gap-6 rounded">
            <img src={logo} className="h-24 rounded"alt="Kanga Logo"></img>
            <p className='text-2xl text-fuchsia-600 mt-2 italic'>New recipes coming soon!</p>
        </div>
    )
}

export default LogoNav
