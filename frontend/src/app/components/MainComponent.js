import styled from "styled-components";
import AllRecordsSquares from "./AllRecordsSquares";
import AllFormats from "./AllFormats";
import Banner from "./Banner";

const StyledUsersChoice = styled.div`
  display: flex;
  align-items: flex-start;
`;

const StyledButtonDiv = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 50px;
`;

const StyledGenerateButton = styled.button`
  border-radius: 1px;
  text-decoration: none;
  background-color: white;
  box-shadow: 5px 5px 5px 0px rgba(0, 0, 0, 0.1);
  font-size: 1.2rem;
  color: rgb(86, 88, 92);
  border: 2px solid rgb(125, 126, 128);
  align-items: center;
  display: inline-flex;
  cursor: pointer;
  padding: 5px 15px;
`;

export default function MainComponent() {
  return (
    <>
      <Banner />
      <StyledUsersChoice>
        <AllRecordsSquares />
        <AllFormats />
      </StyledUsersChoice>
      <StyledButtonDiv>
        <StyledGenerateButton>Generate</StyledGenerateButton>
      </StyledButtonDiv>
    </>
  );
}
