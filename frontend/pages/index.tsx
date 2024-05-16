import { useRouter } from "next/router";
import HeroPage from "./HeroPage";
import NavBar from "../components/NavBar";

export default function Home() {
  return (
    <>
      <NavBar />
      <HeroPage />
    </>
  );
}
