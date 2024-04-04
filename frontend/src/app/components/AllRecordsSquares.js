"use client";
import styled from "styled-components";
import SingleSquare from "./SingleSquare";

const StyledAllSquaresDiv = styled.div`
  display: flex;
  max-width: 50%;
  flex-wrap: wrap;
`;

export default function AllRecordsSquares() {
  return (
    <>
      <StyledAllSquaresDiv>
        <SingleSquare title="Name" color={"rgb(64, 84, 184)"} />
        <SingleSquare title="Surname" color={"rgb(63, 76, 138)"} />
        <SingleSquare title="IBAN" color={"rgb(104, 113, 156)"} />
        <SingleSquare title="IBAN" color={"rgb(104, 113, 156)"} />
        <SingleSquare title="IBAN" color={"rgb(104, 113, 156)"} />
        <SingleSquare title="IBAN" color={"rgb(104, 113, 156)"} />
        <SingleSquare title="IBAN" color={"rgb(104, 113, 156)"} />
        <SingleSquare title="IBAN" color={"rgb(104, 113, 156)"} />
        <SingleSquare title="IBAN" color={"rgb(104, 113, 156)"} />
      </StyledAllSquaresDiv>
    </>
  );
}
