"use client";
import styled from "styled-components";

const StyledAllDiv = styled.div`
  display: flex;
  border-radius: 5px;
  margin: 5px;
  width: 105px;
  height: 100px;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  color: white;
`;

export default function SingleSquare({ title, color }) {
  return (
    <StyledAllDiv
      style={{
        background: color,
      }}
    >
      {title}
    </StyledAllDiv>
  );
}
