import { StatusCodes } from 'http-status-codes'
import { getRunningExpressApp } from '../../utils/getRunningExpressApp'
import { Tool } from '../../database/entities/Tool'
import { getAppVersion } from '../../utils'
import { InternalFlowiseError } from '../../errors/internalFlowiseError'
import { getErrorMessage } from '../../errors/utils'
import { publishToFileCoin, mintNFT, transferERC20} from '../../utils/blockchainHelper'

// import lighthouse from '@lighthouse-web3/sdk';
// import {Contract, ethers, TransactionReceipt, Wallet} from "ethers";
// import ABI from "./abis/AGENTL.json";
// import ERC20ABI from "./abis/AGEN.json";
// import fs from 'fs';


// const rpcUrl = process.env.RPC_URL
// if (!rpcUrl) throw Error("Missing RPC_URL in .env")
// const privateKey = process.env.PRIVATE_KEY
// if (!privateKey) throw Error("Missing PRIVATE_KEY in .env")

// const publishToFileCoin = async(tool_id: string, jsonString: string) => {
//         fs.writeFileSync(tool_id + ".json", jsonString)

//         const apiKey: string | undefined = process.env.LIGHTHOUSE_API_KEY
//         if (!apiKey) throw Error("Missing apiKey in .env")
//         const fileName = tool_id + '.json'
//         const uploadResponse = await lighthouse.upload(
//             fileName,
//             apiKey
//         )
//         const cid = uploadResponse.data.Hash

//         console.log(uploadResponse)

//         fs.unlinkSync(fileName)
//         return cid
//     }

// const mintNFT = async(owner: string, tool_id: string, cid: string) => {
//     const contractAddress = process.env.NTF_CONTRACT_ADDRESS
//     if (!contractAddress) throw Error("Missing NFT_CONTRACT_ADDRESS in .env")
  
//     const provider = new ethers.JsonRpcProvider(rpcUrl)
//     const wallet = new Wallet(
//       privateKey, provider
//     )
//     const contract = new Contract(contractAddress, ABI, wallet)
  
//     // Call the startChat function
//     const transactionResponse = await contract.mint(owner, tool_id, cid);
//     const receipt = await transactionResponse.wait()
//     console.log(`Task sent, tx hash: ${receipt.hash}`)
//     return receipt;
//   }

//   const transferERC20 = async(to: string, value: any) => {
//     const contractAddress = process.env.ERC20_CONTRACT_ADDRESS;
//     const from = process.env.ERC20_FAUCET_ADDRESS;
//     if (!contractAddress) throw Error("Missing ERC20_CONTRACT_ADDRESS in .env")
  
//     const provider = new ethers.JsonRpcProvider(rpcUrl);
//     const wallet = new Wallet(
//       privateKey, provider
//     );
//     const contract = new Contract(contractAddress, ABI, wallet);
  
//     // Call the startChat function
//     const transactionResponse = await contract.transferFrom(from, to, value);
//     const receipt = await transactionResponse.wait();
//     console.log(`Task sent, tx hash: ${receipt.hash}`);
//     return receipt;
//   }

const createTool = async (requestBody: any): Promise<any> => {
    try {
        const appServer = getRunningExpressApp()
        const newTool = new Tool()
        Object.assign(newTool, requestBody)
        const tool = await appServer.AppDataSource.getRepository(Tool).create(newTool)
        const dbResponse = await appServer.AppDataSource.getRepository(Tool).save(tool)

        if(dbResponse.account !== undefined) {
            const owner_id = dbResponse.account;
            const tool_id = dbResponse.id;

            const fileCoinJson = { "toolName": dbResponse.name, "toolId": dbResponse.id, "toolSchema": dbResponse.schema, "toolFunc": dbResponse.func, "toolAccount": dbResponse.account, "toolIcon": dbResponse.iconSrc, "toolDescription": dbResponse.description };
            const jsonString = JSON.stringify(fileCoinJson);

            try {
                const cid = await publishToFileCoin(tool_id, jsonString)
    
                await mintNFT(owner_id, tool_id, cid);                
                await transferERC20(owner_id, 1000000000000);
            }
            catch (error) {
                console.log(error);
            }      
        }

        await appServer.telemetry.sendTelemetry('tool_created', {
            version: await getAppVersion(),
            toolId: dbResponse.id,
            toolName: dbResponse.name
        })
        return dbResponse
    } catch (error) {
        throw new InternalFlowiseError(StatusCodes.INTERNAL_SERVER_ERROR, `Error: toolsService.createTool - ${getErrorMessage(error)}`)
    }
}

const deleteTool = async (toolId: string): Promise<any> => {
    try {
        const appServer = getRunningExpressApp()
        const dbResponse = await appServer.AppDataSource.getRepository(Tool).delete({
            id: toolId
        })
        return dbResponse
    } catch (error) {
        throw new InternalFlowiseError(StatusCodes.INTERNAL_SERVER_ERROR, `Error: toolsService.deleteTool - ${getErrorMessage(error)}`)
    }
}

const getAllTools = async (): Promise<any> => {
    try {
        const appServer = getRunningExpressApp()
        const dbResponse = await appServer.AppDataSource.getRepository(Tool).find()
        return dbResponse
    } catch (error) {
        throw new InternalFlowiseError(StatusCodes.INTERNAL_SERVER_ERROR, `Error: toolsService.getAllTools - ${getErrorMessage(error)}`)
    }
}

const getToolById = async (toolId: string): Promise<any> => {
    try {
        const appServer = getRunningExpressApp()
        const dbResponse = await appServer.AppDataSource.getRepository(Tool).findOneBy({
            id: toolId
        })
        if (!dbResponse) {
            throw new InternalFlowiseError(StatusCodes.NOT_FOUND, `Tool ${toolId} not found`)
        }
        return dbResponse
    } catch (error) {
        throw new InternalFlowiseError(StatusCodes.INTERNAL_SERVER_ERROR, `Error: toolsService.getToolById - ${getErrorMessage(error)}`)
    }
}

const updateTool = async (toolId: string, toolBody: any): Promise<any> => {
    try {
        const appServer = getRunningExpressApp()
        const tool = await appServer.AppDataSource.getRepository(Tool).findOneBy({
            id: toolId
        })
        if (!tool) {
            throw new InternalFlowiseError(StatusCodes.NOT_FOUND, `Tool ${toolId} not found`)
        }
        const updateTool = new Tool()
        Object.assign(updateTool, toolBody)
        await appServer.AppDataSource.getRepository(Tool).merge(tool, updateTool)
        const dbResponse = await appServer.AppDataSource.getRepository(Tool).save(tool)
        return dbResponse
    } catch (error) {
        throw new InternalFlowiseError(StatusCodes.INTERNAL_SERVER_ERROR, `Error: toolsService.updateTool - ${getErrorMessage(error)}`)
    }
}

export default {
    createTool,
    deleteTool,
    getAllTools,
    getToolById,
    updateTool
}
