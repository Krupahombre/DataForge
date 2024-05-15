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
  const [tabSelected, setTabSelected] = useState<string>("");

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
    setTabSelected(data?.[0]?.name || "");
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

  const toggleTabSelected = (name: string) => {
    setTabSelected(name);
  };

  return (
    <div className={styles.mainDiv}>
      <div>
        <button className={styles.returnBtn} onClick={handleBack}>
          <span>Return</span>
          <svg
            viewBox="-5 -5 110 110"
            preserveAspectRatio="none"
            aria-hidden="true"
          >
            <path d="M0,0 C0,0 100,0 100,0 C100,0 100,100 100,100 C100,100 0,100 0,100 C0,100 0,0 0,0" />
          </svg>
        </button>
        <h1 className={styles.resultDisplayTitle}>Generated Data</h1>
      </div>
      {data && (
        <div className={styles.tabsContainer}>
          <div className={styles.resultAllTab}>
            {data.map((record) => (
              <div
                key={record.name}
                className={
                  tabSelected == record.name.toString()
                    ? styles.activeTabs
                    : styles.tabs
                }
                onClick={() => toggleTabSelected(record.name)}
              >
                {record.name}
              </div>
            ))}
          </div>
          <div className={styles.contentTabs}>
            {data.map((record) => (
              <div
                key={record.name}
                className={
                  tabSelected == record.name.toString()
                    ? styles.activeContent
                    : styles.content
                }
              >
                <pre className={styles.resultContentCode}>
                  {record.response}
                </pre>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default ResultDisplayPage;
