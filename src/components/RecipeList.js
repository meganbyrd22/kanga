import React, { useEffect, useState } from 'react';
import axios from 'axios';

const RecipeList = () => {
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/recipes/')  
      .then(response => {
        setRecipes(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the recipes!", error);
      });
  }, []);

  return (
    <div className='h-2/3 grid'>
      <ul className='flex flex-col items-center gap-10 p-10'>
        {recipes.map((recipe, index) => (
          <li key={index} className='flex flex-col items-center shadow-2xl'>
            <h2 className='text-2xl font-bold text-zinc-50'>{recipe.name}</h2>
            <img src={recipe.image_url} alt={recipe.name} className='w-72 h-80 rounded' />
            <p className='italic text-orange-500' dangerouslySetInnerHTML={{ __html: recipe.instructions }}></p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default RecipeList;
