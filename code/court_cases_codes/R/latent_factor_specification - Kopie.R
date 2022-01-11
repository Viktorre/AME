#### general imports
#install.packages('C:/Users/fx236/Documents/AME_files/R/phtt', repos = NULL, type ='source')
#install.packages('haven')
library("phtt")
library('haven')


#### full data  yearly latent factors
raw_data = read_dta("C:/Users/fx236/Documents/AME_files/data_court decisions/Data/final/matched.dta")
data = raw_data[0:269268,]
dim(data)
n <- 67317; T <- 4
print(n*T)
res <- matrix(data$res,n,T)
temp6t410  <- data$temp6t4/1000
temp6t410 <- matrix(temp6t410,n,T)
dim(temp6t410)
press6t4 <- matrix(data$press6t4,n,T)
dew6t4 <- matrix(data$dew6t4,n,T)
prcp6t4 <- matrix(data$prcp6t4,n,T)
wind6t4 <- matrix(data$wind6t4,n,T)
skycover <- matrix(data$skycover,n,T)
ozone <- matrix(data$ozone,n,T)
co <- matrix(data$co,n,T)
summary(Eup(res ~ temp6t410 +press6t4+dew6t4+prcp6t4+wind6t4+skycover+ozone+co,factor.dim = 0))
lf_model<-Eup(res ~ temp6t410 +press6t4+dew6t4+prcp6t4+wind6t4+skycover+ozone+co,factor.dim = 1, dim.criterion = "PC3")
summary(lf_model)
plot(summary(lf_model))



#### full data  testing
raw_data = read_dta("C:/Users/fx236/Documents/AME_files/data_court decisions/Data/final/matched.dta")
data = raw_data[0:269268,]
dim(data)
n <- 89756; T <- 3
print(n*T)
res <- matrix(data$res,n,T)
temp6t410  <- data$temp6t4/1000
temp6t410 <- matrix(temp6t410,n,T)
dim(temp6t410)
press6t4 <- matrix(data$press6t4,n,T)
dew6t4 <- matrix(data$dew6t4,n,T)
prcp6t4 <- matrix(data$prcp6t4,n,T)
wind6t4 <- matrix(data$wind6t4,n,T)
skycover <- matrix(data$skycover,n,T)
ozone <- matrix(data$ozone,n,T)
co <- matrix(data$co,n,T)
summary(Eup(res ~ temp6t410 +press6t4+dew6t4+prcp6t4+wind6t4+skycover+ozone+co,factor.dim = 1,dim.criterion = "PC3"))
lf_model<-Eup(res ~ temp6t410 +press6t4+dew6t4+prcp6t4+wind6t4+skycover+ozone+co, dim.criterion = "PC3")
summary(lf_model)
plot(summary(lf_model))




#### full data  daily latent factors
raw_data = read_dta("C:/Users/fx236/Documents/AME_files/data_court decisions/Data/final/matched.dta")
dim(raw_data)
data = raw_data[0:268324,]
dim(data)
T <- 518; n <- 518
print(n*T)
res <- matrix(data$res,n,T)
temp6t410  <- data$temp6t4/1000
temp6t410 <- matrix(temp6t410,n,T)
dim(temp6t410)
press6t4 <- matrix(data$press6t4,n,T)
dew6t4 <- matrix(data$dew6t4,n,T)
prcp6t4 <- matrix(data$prcp6t4,n,T)
wind6t4 <- matrix(data$wind6t4,n,T)
skycover <- matrix(data$skycover,n,T)
ozone <- matrix(data$ozone,n,T)
co <- matrix(data$co,n,T)
dim(res)
summary(Eup(res ~ temp6t410 +press6t4+dew6t4+prcp6t4+wind6t4+skycover+ozone+co,factor.dim = 0))
lf_model <-  Eup(res ~ temp6t410 +press6t4+dew6t4+prcp6t4+wind6t4+skycover+ozone+co, dim.criterion = "PC3")
summary(lf_model)

plot(summary(lf_model))




###268324	518 * 518






#### 1000 obs test
df <- read.csv(file = 'C:/Users/fx236/Documents/AME_git/AME/code/court_cases_codes/1000obs.csv')
dim(df)
n <- 250; T <- 4
res <- matrix(df$res,n,T)
temp6t410 <- matrix(df$tempmean,n,T)
press6t4 <- matrix(df$press6t4,n,T)
dew6t4 <- matrix(df$dew6t4,n,T)
prcp6t4 <- matrix(df$prcp6t4,n,T)
wind6t4 <- matrix(df$wind6t4,n,T)
skycover <- matrix(df$skycover,n,T)
ozone <- matrix(df$ozone,n,T)
co <- matrix(df$co,n,T)


summary(Eup(res ~ temp6t410 +press6t4+dew6t4+prcp6t4+wind6t4+skycover+ozone+co
            
            , dim.criterion = "PC3",factor.dim = 0))







### Cigar dataset
n <- 46; T <- 30
n <- 690/2/2; T <- 2*2*2
cpi <- matrix(Cigar$cpi, T, n)
l.Consumption <- log(matrix(Cigar$sales, T, n))
l.Price <- log(matrix(Cigar$price, T, n)/cpi)
l.Income <- log(matrix(Cigar$ndi, T, n)/cpi)
d.l.Consumption <- diff(l.Consumption)
d.l.Price <- diff(l.Price)
d.l.Income <- diff(l.Income)

Cigar.Eup <- Eup(d.l.Consumption ~ -1 + d.l.Price + d.l.Income, dim.criterion = "PC3")
Eup(d.l.Consumption ~ -1 + d.l.Price + d.l.Income, dim.criterion = "PC3")


plot(summary(Cigar.Eup))

FEi <- Eup(d.l.Consumption ~ -1 + d.l.Price + d.l.Income,factor.dim = 0, additive.effects = "individual" )
plot(summary(FEi))
summary(FEi)

FEt <- Eup(d.l.Consumption ~ -1 + d.l.Price + d.l.Income,factor.dim = 0, additive.effects = "time" )
plot(summary(FEt))
summary(FEt)

FEit <- Eup(d.l.Consumption ~ -1 + d.l.Price + d.l.Income,factor.dim = 0, additive.effects = "twoways" )
plot(summary(FEit))
summary(FEit)

Pooled  <- Eup(d.l.Consumption ~ -1 + d.l.Price + d.l.Income,factor.dim = 0, additive.effects = "none" )
summary(Pooled)

FEit2 <- Eup(d.l.Consumption ~ -1 + d.l.Price + d.l.Income,factor.dim = 1, additive.effects = "none" )
plot(summary(FEit2))
summary(FEit2)

checkSpecif(Cigar.Eup, level = 0.01)
checkSpecif(FEi, level = 0.01)
checkSpecif(Pooled, level = 0.01)

OptDim(Obj = residuals(Pooled), criteria = c("PC1", "PC2", "PC3", "BIC3", "IC1", "IC2",  "IC3", "IPC1", "IPC2", "IPC3"))


