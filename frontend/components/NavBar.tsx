import React from "react";
import styles from "../styles/Home.module.css";

function NavBar() {
  return (
    <div className={styles.navbar}>
      <style>{`body{
            margin: 0;
        }`}</style>
      <div>DataForge</div>
      <div>Generate your data!</div>
    </div>
  );
}

export default NavBar;
