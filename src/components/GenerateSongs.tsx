import React, { useState } from 'react'
import { GeneratedSongInterface } from '@/types/types'

const GenerateSongs = () => {
  const [ generatedSongs, setGeneratedSongs ] = useState<GeneratedSongInterface[]>([])

  const handleGenerateClick = async () => {
    try {
      const response = await fetch('http://localhost:8080/spotify/organized-data', {
        credentials: 'include',
      });
      if (!response.ok) {
        throw new Error("Could not generate songs");
      }
      const data = await response.json();
      const songs: GeneratedSongInterface[] = []
      for (const song of data.songs) {
        if (song.tracks.items.length === 0) continue;
        const id = song.tracks.items[0].id;
        const artist = song.tracks.items[0].album.artists[0].name;
        const name = song.tracks.items[0].name;
        const url = song.tracks.items[0].external_urls.spotify;
        const duration = song.tracks.items[0].duration_ms;
        const img = song.tracks.items[0].album.images[0].url;
        const album = song.tracks.items[0].album.name;

        const songMetadata = {
          "id": id,
          "artist": artist,
          "name": name,
          "url": url,
          "duration": duration,
          "img": img,
          "album": album
        };
        songs.push(songMetadata);
      }
      setGeneratedSongs(songs);
      console.log("GENERATED:", generatedSongs);
      console.log(data);
    } catch (error) {
      console.error("Cannot generate songs:", error)
    }
  }

  return (
    <div>
      <button 
        className="px-12 py-4 rounded-full bg-[#1ED760] font-bold text-white tracking-widest uppercase transform hover:scale-105 hover:bg-[#21e065] transition-colors duration-200"
        onClick={handleGenerateClick}
      >
        GENERATE SONGS
      </button>
    </div>
  )
}

export default GenerateSongs