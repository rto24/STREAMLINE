export interface UserContextInterface {
  username: string | null,
  setUsername: React.Dispatch<React.SetStateAction<string | null>>;
}

export interface GeneratedSongInterface {
  id: string,
  name: string,
  desc: string,
  img: string,
  album: string
}