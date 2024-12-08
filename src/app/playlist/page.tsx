import React from 'react'
import { SavedSongInterface } from '@/types/types'
import SavedSongs from '@/components/SavedSongs'
import { cookies } from 'next/headers'

async function getUser(): Promise<string> {
  const cookieStore = cookies();
  const token = (await cookieStore).get('spotify_jwt')

  if (!token?.value) {
    console.error('No auth token found in cookies');
    throw new Error('No auth token found');
  }

  try {
    const responseUser = await fetch('http://localhost:8080/auth/user', {
      headers: {
        Authorization: `Bearer ${token.value}`
      },
      cache: 'no-store',
      credentials: 'include'
    });

    if (!responseUser.ok) {
      console.error(`Failed to get user info: ${responseUser.statusText}`);
      throw new Error("Failed to get user info");
    }

    const userData = await responseUser.json();
    return userData.sub
  } catch (error) {
    console.error(error);
    return "User info could not be fetched"
  }
}

async function getSavedSongs(username: string): Promise<SavedSongInterface[]> {
  try {
    const responseSongs = await fetch(`http://localhost:8080/playlist/${username}`, {
      cache: 'no-store'
    });

    if (!responseSongs.ok) {
      console.error(`Failed to get user saved songs: ${responseSongs.statusText}`);
      throw new Error("Failed to get saved songs")
    }

    const songData: SavedSongInterface[] = await responseSongs.json();
    return songData;
  } catch (error) {
    console.error(error)
    return [];
  }
}

const Playlist = async () => {
  const username = await getUser()
  const initialItems = await getSavedSongs(username);
  console.log(initialItems)
  return (
    <>
      <div>Playlist {username}</div>
      <SavedSongs initialItems={initialItems} />
    </>

  )
}

export default Playlist