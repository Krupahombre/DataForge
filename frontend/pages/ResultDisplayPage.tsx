import React, { useState, useEffect, use } from "react";
import getData from "../common/services/getGeneratedData";
import IDisplayDataRecord from "../common/models/IDisplayDataRecord";
import styles from "../styles/Home.module.css";
import { useRouter } from "next/router";
import type { NextPage } from "next";

const ResultDisplayPage: NextPage = () => {
  const [data, setData] = useState<IDisplayDataRecord[]>(
    [] as IDisplayDataRecord[]
  );

  const router = useRouter();

  useEffect(() => {
    const currentUrl = window.location.href;

    const urlParams = new URLSearchParams(currentUrl);

    const format = urlParams.get("format");
    const types = urlParams.getAll("type");

    fetchData(format, types);
  }, []);

  const fetchData = async (format: string, types: string[]) => {
    const response = await getData(format, types);
    const data = formatedData(response);
    setData(data);
  };

  const handleBack = () => {
    router.push("/");
  };

  const formatedData = (response: IDisplayDataRecord[]) => {
    if (response) {
      const formatedStringData = response.map((record) => {
        const formattedResponse = record.response
          .replace(/;/g, ";\n")
          .replace(/CREATE/g, "\nCREATE")
          .replace(/INSERT/g, "\nINSERT")
          .replace(/DROP/g, "\nDROP")
          .replace(/VALUES/g, "\nVALUES");

        return {
          name: record.name,
          response: formattedResponse,
        };
      });
      return formatedStringData;
    }
  };

  return (
    <div className={styles.mainDiv}>
      <div>
        <button onClick={handleBack}>Return</button>
        <h1 className={styles.resultDisplayTitle}>Generated Data</h1>
      </div>
      {data && (
        <div className={styles.resultCodeDisplay}>
          {data.map((record) => (
            <div key={record.name}>
              <p className={styles.resultDisplay}>{record.name}</p>
              <pre className={styles.resultPDisplay}>{record.response}</pre>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default ResultDisplayPage;
