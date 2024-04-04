"use client";
import Image from "next/image";
import styles from "./page.module.css";
import SingleSquare from "./components/SingleSquare";
import styled, { createGlobalStyle } from "styled-components";
import AllRecordsSquares from "./components/AllRecordsSquares";
import AllFormats from "./components/AllFormats";

const GlobalStyles = createGlobalStyle`
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;500;600;700&display=swap');
body{
  background-color: #eee;
  padding: 0;
  margin: 0;
  font-family: 'Open Sans', sans-serif;
}
`;

const StyledUsersChoice = styled.div`
  display: flex;
  align-items: flex-start;
`;

export default function Home() {
  return (
    <>
      <div>
        <h1>Szalom,</h1>
        <h2> this is demo of home page,</h2>
        <h3>innit?</h3>
      </div>
      <StyledUsersChoice>
        <AllRecordsSquares />
        <AllFormats />
      </StyledUsersChoice>
    </>
  );
}
