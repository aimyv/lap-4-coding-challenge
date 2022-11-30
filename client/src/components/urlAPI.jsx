import React, { useState, useEffect } from "react";
import axios from "axios";

const urlAPI = () => {

    const [beers, setBeers] = useState([]);

    //fetching beers from an API with Axios
    async function getShortenedURL() {
        const fetchApi = "http://127.0.0.1:5000/"
        try {
            const apiData = await axios.get(fetchApi);
            const beerNames = apiData.data.map(beer => beer.name)
            setBeers(beerNames)
        } catch (error) {
            console.error(error);
        }
    }

    //API call in useEffect - function being called once when the component is mounted
    useEffect(() => {
        getShortenedURL()
    }, [])

    return <>
            <h2>Beers</h2>
            { beers.map(b => <li>{b}</li>) }
           </>
}

export default urlAPI;
