export interface UserContextInterface {
  username: string | null,
  setUsername: React.Dispatch<React.SetStateAction<string | null>>;
}

export interface GeneratedSongInterface {
  id: string,
  artist: string,
  name: string,
  url: string,
  duration: number,
  img: string,
  album: string,
}

export interface SongCardInterface {
  artist: string,
  name: string,
  img: string,
  ctaText: string,
  ctaLink: string
}