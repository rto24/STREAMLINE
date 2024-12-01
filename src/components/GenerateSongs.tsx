import React, { useState } from 'react'
import { GeneratedSongInterface, SongCardInterface } from '@/types/types'
import ExpandableCardDemo from './blocks/expandable-card-demo-standard'
import { MultiStepLoader } from './ui/multi-step-loader'
import { loadingText } from '@/data/data'
import { g } from 'framer-motion/m'

const GenerateSongs = () => {
  const [ generatedSongs, setGeneratedSongs ] = useState<GeneratedSongInterface[]>([]);
  const [ displayedSongs, setDisplaySongs ] = useState<SongCardInterface[]>([]);
  const [ loadingSongs, setLoadingSongs ] = useState<boolean>(false);

  const handleGenerateClick = async () => {
    setLoadingSongs(true);
    try {
      const response = await fetch('http://localhost:8080/spotify/organized-data', {
        credentials: 'include',
      });
      if (!response.ok) {
        throw new Error("Could not generate songs");
      }
      const data = await response.json();
      const songs: GeneratedSongInterface[] = [];
      const displaySongs: SongCardInterface[] = [];

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

        const displayCard = {
          "artist": artist,
          "name": name,
          "img": img,
          "ctaText": "Play",
          "ctaLink": url
        }
        displaySongs.push(displayCard);
      }
      
      setGeneratedSongs((prevSongs) => [...prevSongs, ...songs]);
      setDisplaySongs((prevDisplaySongs) => [...prevDisplaySongs, ...displaySongs]);
      setLoadingSongs(false);
      console.log("GENERATED:", generatedSongs);
      console.log(data);
    } catch (error) {
      console.error("Cannot generate songs:", error)
    }
  }

  return (
    <>
      <div>
        <button 
          className="px-12 py-4 rounded-full bg-[#1ED760] font-bold text-white tracking-widest uppercase transform hover:scale-105 hover:bg-[#21e065] transition-colors duration-200"
          onClick={handleGenerateClick}
          >
          GENERATE SONGS
        </button>
        <ExpandableCardDemo cards={displayedSongs}/>
      </div>

      {loadingSongs &&
        (
          <MultiStepLoader 
            loadingStates={loadingText}
            loading={true}
            duration={2000}
            loop={false}
          />
        )
      }
    </>
  )
}

export default GenerateSongs