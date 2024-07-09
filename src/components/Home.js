import LogoNav from "./LogoNav"
const Home = () => {

    return (
        <section>
            <LogoNav />
            <div className="h-screen bg-gradient-to-r from-orange-400 to-orange-200 flex justify-center items-center gap-10 p-16">
                
                <h1 className="text-6xl font-bold text-zinc-50 w-1/3">Summer recipes you have to try!</h1>
                <div className="h-5/6 w-3/6 bg-gradient-to-l from-fuchsia-400 to-fuchsia-200 rounded"></div>
            </div>
        </section>
    )
}

export default Home