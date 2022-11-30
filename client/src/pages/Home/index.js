import React, { useContext, useState } from 'react'
import axios from "axios"

export default function Home() {

  const [longUrl, setLongUrl] = useState('')
  const [shortUrl, setShortUrl] = useState('')

  const handleSubmit = event => {
    event.preventDefault();
    let protocol_ok = longUrl.startsWith('http://') || longUrl.startsWith('https://') || longUrl.startsWith('ftp://')
    if (protocol_ok) {
      alert('URL SHRTND 😎')
      axios.post('http://localhost:5000/urls', {
        'long_path': longUrl
      }).then(function (response) {
        setShortUrl(response.data['short_path'])
      }).catch(function (error) {
        console.log(error);
      });
    } else {
      alert('😳 Oops! That wasn\'t a valid url. Please enter a valid url.')
    }
    
  }

  const handleText = e => {
    setLongUrl(e.target.value)
  }

  const seeLink = url => {
    if (url !== '') {
      return (<>
      SHRTND 🔗: <a href={`http://localhost:5000/${shortUrl}`} target='_blank'>{`http://localhost:5000/${shortUrl}`}</a>
      </>
      )
    }
  }

  return (
    <div class='center'>
      <h1>SH✂️RT✂️NR</h1>
      <hr />
      <div>
        <form onSubmit={handleSubmit} id="urlInput">
            <label>Enter URL to SHRTN: <br />
              <input type="text" longurl={longUrl} onChange={handleText} placeholder='Enter URL' />
            </label>
            <button type="submit">SHRTN!</button>
        </form>
      </div>
      <br />
      {seeLink(shortUrl)}
    </div>
  )
}
