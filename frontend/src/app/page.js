"use client";
import Image from "next/image";
import styles from "./page.module.css";
import { createGlobalStyle } from "styled-components";
import MainComponent from "./components/MainComponent";

const GlobalStyles = createGlobalStyle`
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;500;600;700&display=swap');
body{
  background-color: #eee;
  padding: 0;
  margin: 0;
  font-family: 'Open Sans', sans-serif;
}
`;

export default function Home() {
  return (
    <>
      <MainComponent />
    </>
  );
}
