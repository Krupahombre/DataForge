"use client";
import styled from "styled-components";
import SingleSquare from "./SingleSquare";

const StyledMainDiv = styled.div`
  max-width: 50%;
`;

const StyledAllSquaresDiv = styled.div`
  display: flex;
  flex-wrap: wrap;
  height: auto;
  justify-content: flex-start;
  align-itmes: flex-start;
  max-width: 600px;
`;

const StyledInfo = styled.label`
  display: flex;
  align-itmes: center;
  margin-bottom: 5px;
  font-size: 1.2rem;
  color: rgb(86, 88, 92);
  margin-left: 5px;
`;

export default function AllFormats() {
  return (
    <StyledMainDiv>
      <StyledInfo>Choose a data format:</StyledInfo>
      <StyledAllSquaresDiv>
        <SingleSquare title="JSON" color={"rgb(62, 99, 158)"} />
        <SingleSquare title="BJSON" color={"rgb(62, 99, 158)"} />
        <SingleSquare title="Oracle" color={"rgb(62, 99, 158)"} />
        <SingleSquare title="MySQL" color={"rgb(62, 99, 158)"} />
        <SingleSquare title="FireBird" color={"rgb(62, 99, 158)"} />
      </StyledAllSquaresDiv>
    </StyledMainDiv>
  );
}
