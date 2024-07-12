import LogoNav from "./LogoNav";
import RecipeList from './RecipeList';
const Home = () => {

    return (
        <section>
            <LogoNav />
            <div className="h-full bg-gradient-to-r from-orange-400 to-orange-200 flex justify-center gap-10 p-16">
                <div className="flex flex-col items-center gap-40">
                    <h1 className="text-6xl font-bold text-zinc-50 w-2/3 ">Summer recipes you have to try!</h1>
                    <p className="text-3xl  text-zinc-50 w-2/3">Fresh flavors to change things up and get in healthy sides.</p>
                    <p className="text-3xl  text-zinc-50 w-2/3">Try them at your next barbecue or just for a different family dinner during the week!</p>
                    <p className='text-4xl font-bold text-fuchsia-600 mt-2 italic mt-40'>New recipes coming soon!</p>
                </div>
                <div className="h-4/6 w-4/6 bg-gradient-to-l from-fuchsia-400 to-fuchsia-200 rounded">
                <RecipeList />
                </div>
            </div>
        </section>
    )
}

export default Home
