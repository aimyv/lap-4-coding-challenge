import React, { useContext, useState } from 'react'

export default function Home() {

  const [longUrl, setLongUrl] = useState('')

  function handleSubmit(e) {
    e.preventDefault()
  }

  return (
    <div>
      <h1>SH&#9988;RT&#9988;N&#9988;R</h1>
      <div>
        <form>
          <label>
            <input type="text" longurl="longurl" />
            </label>
            <input type="submit" value="SHRTN!" />
        </form>
      </div>
    </div>
  )
}
