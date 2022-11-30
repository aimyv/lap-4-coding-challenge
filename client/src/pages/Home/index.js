import React, { useContext, useState } from 'react'
import axios from "axios"

export default function Home() {

  const [longUrl, setLongUrl] = useState('')
  const [shortUrl, setShortUrl] = useState('')

  const handleSubmit = event => {
    event.preventDefault();
    alert('URL SHRTND!')
    // console.log(longUrl);
    axios.post('http://localhost:5000/urls', {
      'long_path': longUrl
    }).then(function (response) {
      console.log(response.data['short_path']);
      setShortUrl(response.data['short_path'])
    }).catch(function (error) {
      console.log(error);
    });
  }

  const handleText = e => {
    setLongUrl(e.target.value)
  }

  return (
    <div>
      <h1>SH&#9988;RT&#9988;N&#9988;R</h1>
      <div>
        <form onSubmit={handleSubmit} id="urlInput">
          <label>
            <input type="text" longurl={longUrl} onChange={handleText} />
            </label>
            <button type="submit">SHRTN!</button>
        </form>
      </div>
    </div>
  )
}
