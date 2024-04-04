"use client";
import styled from "styled-components";
import SingleSquare from "./SingleSquare";

const StyledAllSquaresDiv = styled.div`
  display: flex;
  max-width: 50%;
  flex-wrap: wrap;
  height: auto;
  justify-content: flex-start;
  align-itmes: flex-start;
`;

export default function AllFormats() {
  return (
    <>
      <StyledAllSquaresDiv>
        <SingleSquare title="JSON" color={"rgb(104, 113, 156)"} />
        <SingleSquare title="BJSON" color={"rgb(104, 113, 156)"} />
        <SingleSquare title="Oracle" color={"rgb(104, 113, 156)"} />
        <SingleSquare title="MySQL" color={"rgb(104, 113, 156)"} />
        <SingleSquare title="FireBird" color={"rgb(104, 113, 156)"} />
      </StyledAllSquaresDiv>
    </>
  );
}
