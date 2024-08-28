import { ethers } from "hardhat";

async function main() {
  const [deployer] = await ethers.getSigners();
  console.log("Deploying contracts with the account:", deployer.address);

  const NiftyITPrediction =
    await ethers.getContractFactory("NiftyITPrediction");
  const niftyITPrediction = await NiftyITPrediction.deploy();

  await niftyITPrediction.waitForDeployment();
  console.log(
    "NiftyITPrediction deployed to:",
    await niftyITPrediction.getAddress(),
  );
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
