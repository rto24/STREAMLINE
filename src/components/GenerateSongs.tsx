import React, { useState } from 'react'
import { GeneratedSongInterface, SongCardInterface } from '@/types/types'
import ExpandableCardDemo from './blocks/expandable-card-demo-standard'
import { MultiStepLoader } from './ui/multi-step-loader'
import { loadingText, typewriterWords } from '@/data/data'
import { TypewriterEffectSmooth } from './ui/typewriter-word-effect'
import { FadeInEffect } from './ui/fade-in-text'
import { useUser } from '@/context/UserContext'

const GenerateSongs = () => {
  const [ generatedSongs, setGeneratedSongs ] = useState<GeneratedSongInterface[]>([]);
  const [ displayedSongs, setDisplaySongs ] = useState<SongCardInterface[]>([]);
  const [ loadingSongs, setLoadingSongs ] = useState<boolean>(false);

  const { username } = useUser();

  const welcomeMessage = [
    { text: "Welcome" },
    { text: "back" },
    { text: username }
  ];

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
          "id": id,
          "artist": artist,
          "name": name,
          "img": img,
          "ctaText1": "Play",
          "ctaText2": "Save",
          "ctaLink": url
        }
        displaySongs.push(displayCard);
      }
      
      setGeneratedSongs((prevSongs) => {
        const existingIds = new Set(prevSongs.map((song) => song.id));
        return [...prevSongs, ...songs.filter((song) => !existingIds.has(song.id))];
      });
      
      setDisplaySongs((prevDisplaySongs) => {
        const existingKeys = new Set(prevDisplaySongs.map((song) => song.name + song.artist));
        return [...prevDisplaySongs, ...displaySongs.filter((song) => !existingKeys.has(song.name + song.artist))];
      });
      setLoadingSongs(false);
      console.log("GENERATED:", generatedSongs);
      console.log(data);
    } catch (error) {
      console.error("Cannot generate songs:", error)
    }
  }

  const handleSaveClick = async (username: string | null, song: SongCardInterface) => {
    const formattedSong = {
      artist: song.artist,
      name: song.name,
      img: song.img,
      ctaLink: song.ctaLink, 
  };

    try {
      const response = await fetch(`http://localhost:8080/playlist/${username}`, {
        method: 'POST',
        credentials: 'include',
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          playlists: [formattedSong],
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to save the song to the playlist")
      }
      const data = await response.json();
      console.log("Song saved:", data)
    } catch (error) {
      console.error("Error saving song", error)
    }
  }

  return (
    <>
      <div className="flex flex-col justify-center">
        <TypewriterEffectSmooth className="justify-center" words={typewriterWords} />
        <FadeInEffect words={welcomeMessage} className="font-bold mx-auto"/>
        <button 
          className="mx-auto px-12 py-4 w-1/4 rounded-full bg-[#1ED760] font-bold text-white tracking-widest uppercase transform hover:scale-105 hover:bg-[#21e065] transition-colors duration-200"
          onClick={handleGenerateClick}
          >
          GENERATE SONGS
        </button>
        <ExpandableCardDemo saveToPlaylist={(song: SongCardInterface) => handleSaveClick(username, song)} cards={displayedSongs}/>
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