import { useRouter } from "next/router";
import HeroPage from "./HeroPage";
import NavBar from "../components/NavBar";
import styles from "../styles/Home.module.css";

export default function Home() {
  return (
    <div className={styles.MainHeroDiv}>
      <NavBar />
      <HeroPage />
    </div>
  );
}
