import React, { useState } from "react";
import styles from "../styles/Home.module.css";

function NavBar() {
  const [showHelp, setShowHelp] = useState(false);
  return (
    <>
      <div className={styles.navbar}>
        <style>{`body{
            margin: 0;
        }`}</style>
        <div>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            strokeWidth="1.5"
            stroke="currentColor"
            className="w-6 h-6"
            style={{ width: "24px", height: "24px" }}
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M20.25 6.375c0 2.278-3.694 4.125-8.25 4.125S3.75 8.653 3.75 6.375m16.5 0c0-2.278-3.694-4.125-8.25-4.125S3.75 4.097 3.75 6.375m16.5 0v11.25c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125V6.375m16.5 0v3.75m-16.5-3.75v3.75m16.5 0v3.75C20.25 16.153 16.556 18 12 18s-8.25-1.847-8.25-4.125v-3.75m16.5 0c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125"
            />
          </svg>
          DataForge
        </div>
        <div onClick={() => setShowHelp(!showHelp)} className={styles.helpButton}>Help</div>
        <div>Generate your data!</div>
      </div>
      {showHelp && (
        <div className={styles.helpOverlay} onClick={() => setShowHelp(false)}>
          <div className={styles.helpContent} onClick={(e) => e.stopPropagation()}>
            <h2>Help</h2>
            <p>
              DataForge is a tool for generating realistic test data. You can create tables with various fields and data types, then generate data in multiple formats including JSON, MySQL, PostgreSQL, and CSV.
            </p>
            <p>
              To get started, select the desired output format, specify the number of records to generate, and click the "Generate" button. You can also define custom tables and add fields to suit your needs.
            </p>

            <p>In case of any conserns please reach to our support: kacper4553@gmail.com</p>


          </div>
        </div>
      )}
    </>
  );
}

export default NavBar;
