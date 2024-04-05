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
        <SingleSquare title="Name" color={"rgb(63, 76, 138)"} />
        <SingleSquare title="Surname" color={"rgb(63, 76, 138)"} />
        <SingleSquare title="IBAN" color={"rgb(63, 76, 138)"} />
        <SingleSquare title="IBAN" color={"rgb(63, 76, 138)"} />
        <SingleSquare title="IBAN" color={"rgb(63, 76, 138)"} />
        <SingleSquare title="IBAN" color={"rgb(63, 76, 138)"} />
        <SingleSquare title="IBAN" color={"rgb(63, 76, 138)"} />
        <SingleSquare title="IBAN" color={"rgb(63, 76, 138)"} />
        <SingleSquare title="IBAN" color={"rgb(63, 76, 138)"} />
      </StyledAllSquaresDiv>
    </>
  );
}
