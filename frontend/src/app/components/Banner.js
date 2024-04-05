import styled from "styled-components";

const StyledMajorComponent = styled.div``;

const StyledTitle = styled.h1`
  display: flex;
  align-itmes: center;
  justify-content: center;
  color: rgb(86, 88, 92);
  font-size: 2.5rem;
`;

const StyledSubTitle = styled.label`
  display: flex;
  align-itmes: center;
  justify-content: center;
  margin-bottom: 20px;
  font-size: 1.4rem;
  color: rgb(86, 88, 92);
`;

export default function Banner() {
  return (
    <StyledMajorComponent>
      <StyledTitle>Data Forge</StyledTitle>
      <StyledSubTitle>Generate your data!</StyledSubTitle>
    </StyledMajorComponent>
  );
}
