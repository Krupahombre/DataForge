import React, { useState, useEffect, use } from "react";
import getData from "../../common/services/getGeneratedData";
import IResponse from "../../common/models/IResponse";
import "../../styles/Home.module.css";
const ResultDisplayPage = () => {
  const [data, setData] = useState<IResponse>(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const response = await getData();
    console.log(response);
    setData(response);
  };

  return (
    <div className="resultCodeDisplay">
      <h1>Generated Data</h1>
      {data && (
        <div>
          <h3>Person</h3>
          <p>{data.person}</p>
          <h3>IBAN</h3>
          <p>{data.iban}</p>
        </div>
      )}
    </div>
  );
};

export default ResultDisplayPage;
