"use client";
import styled from "styled-components";
import SingleSquare from "./SingleSquare";

const StyledMainDiv = styled.div`
  max-width: 50%;
`;

const StyledAllSquaresDiv = styled.div`
  display: flex;
  flex-wrap: wrap;
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

export default function AllRecordsSquares() {
  return (
    <StyledMainDiv>
      <StyledInfo>Choose the types of data:</StyledInfo>
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
    </StyledMainDiv>
  );
}
