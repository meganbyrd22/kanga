import logo from '../assets/KangacookLogo.png'
const LogoNav = () => {

    return (
        <div className="h-32 bg-zinc-50 w-screen flex position-absolute justify-end p-12 items-center gap-6 rounded">
            <img src={logo} className="h-24 rounded"alt="Kanga Logo"></img> 
        </div>
    )
}

export default LogoNav

